import React, {useEffect, useState} from 'react';
import Toolbar from "@material-ui/core/Toolbar";
import AppBar from "@material-ui/core/AppBar";
import Typography from "@material-ui/core/Typography";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from '@material-ui/icons/Menu';
import makeStyles from "@material-ui/core/styles/makeStyles";
import Drawer from "@material-ui/core/Drawer";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import List from "@material-ui/core/List";
import Divider from "@material-ui/core/Divider";
import MoreVertIcon from '@material-ui/icons/MoreVert';
import Avatar from "@material-ui/core/Avatar";
import axios from 'axios';
import jwt_decode from "jwt-decode";
import HomeIcon from '@material-ui/icons/Home';
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListSubheader from "@material-ui/core/ListSubheader";
import AnnouncementOutlinedIcon from '@material-ui/icons/AnnouncementOutlined';
import ListItemAvatar from "@material-ui/core/ListItemAvatar";
import Button from "@material-ui/core/Button";
import Popper from "@material-ui/core/Popper";
import Grow from "@material-ui/core/Grow";
import Paper from "@material-ui/core/Paper";
import MenuItem from "@material-ui/core/MenuItem";
import MenuList from "@material-ui/core/MenuList";
import ClickAwayListener from "@material-ui/core/ClickAwayListener";
import Dialog from "@material-ui/core/Dialog";
import DialogTitle from "@material-ui/core/DialogTitle";
import DialogContent from "@material-ui/core/DialogContent";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContentText from "@material-ui/core/DialogContentText";
import TextField from "@material-ui/core/TextField";
import AlertNotification from "./helper/Alert";

const useStyles = makeStyles((theme) => ({
    root: {
      flexGrow: 1,
    },
    title: {
      flexGrow: 1,
    },
    header: {
        marginBottom: 70,
    },
    Drawer:{
        minWidth: 170,
    },
    Help:{
        marginTop: 'auto',
    },
    nested: {
        paddingLeft: theme.spacing(4),
      },
  }));



export default function Header(props) {
  const classes = useStyles();
  const [serverOpen, setServerOpen] = useState(false);
  const anchorRef = React.useRef(null);
  const server = localStorage.getItem('server') || null;
  const local_servers = JSON.parse(localStorage.getItem('servers')) || [];
  const [current_server, setCurrentServer] = useState(server);
  const [dialogFeedBack, setDialogFeedBack] = useState(false);
  const [messageFeedBack, setMessageFeedBack] = useState('');
  const [notify, setNotify] = useState({open:false, message:'', type: 'success'});
  const [errors, setErrors] = useState({});
  const clear_errors = (name) => {
        if (errors) {
            const copyErrors = {...errors};
            delete copyErrors[name];
            setErrors(copyErrors)
        }
    };

  const set_server = (title) => {
    localStorage.setItem('server', title);
    setCurrentServer(title);
    setServerOpen(false);
  };

  const send_feedback = () => {
      if (messageFeedBack){
        setDialogFeedBack(false);
        setMessageFeedBack('');
        setLeftDrawerOpen(false);
        axios.post('/api/help/feedback/', {
                message: messageFeedBack,
            })
            .then(response => {
                    setNotify({open:true, message: 'Сообщение успешно отправлено, спасибо за помощь!',
                        type: 'success'})
            })
            .catch(error => {
                console.error(error.response);
            });
      }
      else {
          setErrors({'message': 'Поле должно быть заполнено'})
      }

  };

  useEffect(() => {
     let local_servers = localStorage.getItem('servers');
     if (!local_servers){
         axios.get('/api/pw/servers/')
            .then(response => {
                localStorage.setItem('servers', JSON.stringify(response.data.results));
            })
            .catch(error => {
                console.log('error', error.response);
            });
     }

  }, []);

  // DRAWER
  //  ---------LEFT DRAWER---------
  const [leftDrawerOpen, setLeftDrawerOpen] = useState(false);
  const handleToggleLeftDrawer = () => {
    setLeftDrawerOpen(!leftDrawerOpen);
  };
  const leftDrawer = (
      <Drawer anchor="left" open={leftDrawerOpen} onClose={handleToggleLeftDrawer}>
            <List className={classes.Drawer}>
                <ListItem button={false} component="a" href="http://localhost:3000">
                    <ListItemAvatar>
                        <Avatar className={classes.avatar}
                                  src="/logo.png"
                                  variant="square"
                        />
                    </ListItemAvatar>
                  <ListItemText primary="Hevent"
                                secondary="Описание"/>
                </ListItem>
            </List>
            <Divider />
             <List
              component="nav"
              className={classes.root}
            >
              <ListItem component="a" button href={'/'}>
                  <ListItemIcon>
                    <HomeIcon />
                  </ListItemIcon>
                <ListItemText primary="Главная" />
              </ListItem>
            </List>
            <Divider />
            <List className={classes.Help}
                  subheader={
                    <ListSubheader component="div" id="nested-list-subheader">
                      Помощь проекту
                    </ListSubheader>
                  }
                  component="nav"

            >
                <ListItem className={classes.nested} button onClick={() => setDialogFeedBack(true)}>
                  <ListItemIcon>
                    <AnnouncementOutlinedIcon />
                  </ListItemIcon>
                  <ListItemText primary="Оставить отзыв" secondary="Или сообщить об ошибке"/>
                </ListItem>
            </List>

          <Dialog open={dialogFeedBack} onClose={() => setDialogFeedBack(false)}>
            <DialogTitle>Обратная связь</DialogTitle>
            <DialogContent>
              <DialogContentText>
                  Привет, Ваше мнение очень важно в развитии данного проекта!
                  Отправленное сообщение будет видно только разработчику и будет доставлено анонимно.
              </DialogContentText>
              <TextField
                autoFocus
                margin="dense"
                id="comment"
                type="text"
                fullWidth
                multiline
                error={!!errors.message}
                helperText={!!errors.message ? errors.message : "Опишите подробнее Вашу проблему или предложение"}
                value={messageFeedBack}
                onChange={(e) => {
                    setMessageFeedBack(e.target.value);
                    clear_errors('message');
                }}
              />
            </DialogContent>
            <DialogActions>
              <Button onClick={() => setDialogFeedBack(false)} color="primary">
                Закрыть
              </Button>
              <Button onClick={send_feedback} color="primary">
                Отправить
              </Button>
            </DialogActions>
          </Dialog>
        </Drawer>
  );
  //  ---------RIGHT DRAWER---------
  const [rightDrawerOpen, setRightDrawerOpen] = useState(false);
  const handleToggleRightDrawer = () => {
      setRightDrawerOpen(!rightDrawerOpen);
  };

  const logout = () => {
      let token = props.cookie.access;

      let decode = jwt_decode(token);
      let exp = decode.exp;
      let options = {
        path: '/',
        maxAge: exp,
      };
      props.removeCookie('access', options);
      axios.defaults.headers.common = {};
  };


  const rightDrawer = props.isAuth ? (
        <Drawer anchor="right" open={rightDrawerOpen} onClose={handleToggleRightDrawer}>
            <List className={classes.Drawer}>
                <ListItem button component="a" href="/profile/">
                  <ListItemText primary="Настройки"/>
                </ListItem>
                <Divider />
                <ListItem button onClick={logout}>
                  <ListItemText primary="Выйти"/>
                </ListItem>
            </List>
        </Drawer>
  ) : (
      <Drawer anchor="right" open={rightDrawerOpen} onClose={handleToggleRightDrawer}>
            <List className={classes.Drawer}>
                <ListItem button component="a" href="/login/">
                  <ListItemText primary="Войти" />
                </ListItem>
                <ListItem button component="a" href="/register/">
                  <ListItemText primary="Регистрация"/>
                </ListItem>
            </List>
        </Drawer>
  );

  return (
    <div className={classes.header}>
        <AppBar position="fixed">
          <Toolbar>
            <IconButton
                edge="start"
                color="inherit"
                aria-label="menu"
                onClick={handleToggleLeftDrawer}
            >
              <MenuIcon />
            </IconButton>
            <Typography variant="h6" className={classes.root}>
                {props.title}
            </Typography>
          <Button edge="end"
                  color="inherit"
                  aria-label='Choose server'
                  ref={anchorRef}
                  onClick={(e) => setServerOpen(!serverOpen)}
          >
              {current_server || 'Сервер'}
          </Button>
          <Popper open={serverOpen} anchorEl={anchorRef.current} role={undefined} transition disablePortal>
          {({ TransitionProps, placement }) => (
            <Grow
              {...TransitionProps}
              style={{ transformOrigin: placement === 'bottom' ? 'center top' : 'center bottom' }}
            >
              <Paper>
                <ClickAwayListener onClickAway={(e) => setServerOpen(false)}>
                  <MenuList autoFocusItem={serverOpen} id="menu-list-grow">
                      {local_servers.map((server, index) => <MenuItem key={server.id} onClick={() => set_server(server.title)}>
                                                                  {server.title}
                                                              </MenuItem>)}
                  </MenuList>
                </ClickAwayListener>
              </Paper>
            </Grow>
          )}
        </Popper>
            <IconButton
                edge="end"
                color="inherit"
                aria-label="menu"
                onClick={handleToggleRightDrawer}
            >
              <MoreVertIcon />
            </IconButton>
          </Toolbar>
        </AppBar>
        {leftDrawer}
        {rightDrawer}
        <AlertNotification notify={notify} setNotify={setNotify}/>
    </div>
  );
}
