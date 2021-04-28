import React, {useState} from 'react';
import {useSnackbar} from 'notistack';
import clsx from 'clsx';

import AppBar from '@material-ui/core/AppBar';
import Grid from '@material-ui/core/Grid';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Toolbar from '@material-ui/core/Toolbar';
import Chip from '@material-ui/core/Chip';
import Autocomplete from '@material-ui/lab/Autocomplete';
import TextField from '@material-ui/core/TextField';
import Cookies from 'universal-cookie';


export default function Header({classes, open, onDrawerToggle, user}) {
  const cookie = new Cookies();
  const {enqueueSnackbar} = useSnackbar();
  const [course, setCourse] = useState((() => {
    try {
      return JSON.parse(atob(cookie.get('course')));
    } catch (_) {
    }
    return null;
  })());

  return (
    <React.Fragment>
      <AppBar
        color="primary"
        elevation={0}
        position="fixed"
        className={clsx(classes.appBar, {
          [classes.appBarShift]: open,
        })}
      >
        <Toolbar>
          <Grid container spacing={1} alignItems="center">
            <Grid item>
              <IconButton
                color="inherit"
                aria-label="open drawer"
                onClick={onDrawerToggle}
                className={classes.menuButton}
              >
                <MenuIcon/>
              </IconButton>
            </Grid>
            <Grid item xs/>
            <Grid item>
              <div style={{display: 'flex', flexDirection: 'row'}}>
                {user?.is_admin ? (
                  <Autocomplete
                    options={user.admin_for ?? []}
                    getOptionLabel={(option) => option.name}
                    value={course}
                    style={{width: 200}}
                    onChange={(_, e) => {
                      cookie.remove('course', {path: '/'});
                      if (!!e) {
                        cookie.set('course', btoa(JSON.stringify(e)), {path: '/'});
                        enqueueSnackbar(
                          'You may need to reload the page for context change to take effect.',
                          {variant: 'warning'},
                        );
                      }
                      setCourse(e);
                    }}
                    renderInput={(params) => (
                      <TextField {...params} label="Context"/>
                    )}
                  />
                ) : null}
                <div className={classes.avatar}>
                  {user?.netid && <Chip clickable label={user?.netid}/>}
                </div>
              </div>
            </Grid>
          </Grid>
        </Toolbar>
      </AppBar>
    </React.Fragment>
  );
}
