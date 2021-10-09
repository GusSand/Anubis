import {makeStyles} from '@material-ui/core/styles';

export const useStyles = makeStyles((theme) => ({
  submissionContainer: {
    color: theme.palette.white,
    flexGrow: 1,
    minWidth: 1000,
    maxWidth: 1000,
    minHeight: 500,
    backgroundColor: theme.palette.dark.blue['200'],
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'space-between',
    padding: `${theme.spacing(2.5)}px`,
    borderRadius: `${theme.spacing(1.25)}px`,
    margin: theme.spacing(5),
  },
  headerContainer: {
    position: 'absolute',
    flexGrow: 1,
    minWidth: 200,
    maxWidth: 200,
    backgroundColor: '#21262D',
  },
  gridList: {
    backgroundColor: theme.palette.dark.blue['200'],
  },
  failedContainer: {
    position: 'relative',
    color: theme.palette.color.red,
    top: -theme.spacing(6),
    right: -theme.spacing(9),
    flexGrow: 1,
    fontSize: '18px',
    minWidth: 200,
    maxWidth: 200,
    backgroundColor: '#21262D',
  },
  statsContainer: {
    position: 'relative',
    color: theme.palette.white,
    top: -theme.spacing(6),
    right: -theme.spacing(9),
    fontSize: '13px',
    flexGrow: 1,
    minWidth: 500,
    maxWidth: 500,
    backgroundColor: '#21262D',
  },
}));
