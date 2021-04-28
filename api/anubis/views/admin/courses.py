from flask import Blueprint
from sqlalchemy.exc import IntegrityError, DataError

from anubis.models import db, Course
from anubis.utils.users.auth import require_admin, require_superuser
from anubis.utils.data import row2dict
from anubis.utils.http.decorators import json_response, json_endpoint
from anubis.utils.http.https import success_response, error_response
from anubis.utils.lms.course import get_visible_courses, assert_course_superuser

courses_ = Blueprint("admin-courses", __name__, url_prefix="/admin/courses")


@courses_.route("/list")
@require_admin()
@json_response
def admin_courses_list():
    professor_courses, ta_courses = get_visible_courses()

    return success_response({
        "ta_courses": [
            {"join_code": course.id[:6], **row2dict(course)} for course in ta_courses
        ],
        "professor_courses": [
            {"join_code": course.id[:6], **row2dict(course)} for course in professor_courses
        ],
    })


@courses_.route("/new")
@require_superuser()
@json_response
def admin_courses_new():
    course = Course(
        name="placeholder",
        course_code="placeholder",
        section="a",
        professor="placeholder",
    )
    db.session.add(course)
    db.session.commit()

    return success_response({
        "course": course.data,
        "status": "Created new course",
    })


@courses_.route("/save", methods=["POST"])
@require_admin()
@json_endpoint(required_fields=[("course", dict)])
def admin_courses_save_id(course: dict):
    course_id = course.get("id", None)
    db_course = Course.query.filter(Course.id == course_id).first()

    if db_course is None:
        return error_response("Course not found.")

    assert_course_superuser(course_id)

    for key, value in course.items():
        setattr(db_course, key, value)

    try:
        db.session.commit()
    except (IntegrityError, DataError) as e:
        db.session.rollback()
        return error_response("Unable to save " + str(e))

    return success_response({"course": db_course.data, "status": "Changes saved."})
