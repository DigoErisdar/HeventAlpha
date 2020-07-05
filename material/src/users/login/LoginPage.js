
import React, {useState} from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import AlertNotification from "../../helper/Alert";
import Dialog from "@material-ui/core/Dialog";
import DialogTitle from "@material-ui/core/DialogTitle";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogActions from "@material-ui/core/DialogActions";
import {setToken} from '../../helper/api';
import jwt_decode from 'jwt-decode';
import Loading from "../../helper/loading";
import axios from 'axios';


const useStyles = makeStyles((theme) => ({
  root: {
    height: '100vh',
  },
  image: {
    backgroundImage: 'url(https://i.pinimg.com/originals/ca/77/24/ca77244c4831303582e721542151b33d.png)',
    backgroundRepeat: 'no-repeat',
    backgroundColor:
      theme.palette.type === 'light' ? theme.palette.grey[50] : theme.palette.grey[900],
    backgroundSize: 'content',
    backgroundPosition: 'center',
  },
  paper: {
    margin: theme.spacing(8, 4),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
  },
  form: {
    width: '100%',
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
  backdrop: {
    zIndex: theme.zIndex.drawer + 1,
    color: '#fff',
  },
}));

export default function LoginPage(props) {
  const classes = useStyles();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [remember, setRemember] = useState(true);
  const [notify, setNotify] = useState({open:false, message:'', type: 'success'});
  const [resetOpen, setResetOpen] = useState(false);
  const [resetEmail, setResetEmail] = useState("");
  const [loading, setLoading] = useState(false);

  const authenticate = (event) => {
    event.preventDefault();
    setLoading(true);
    axios.post('/api/token/', {
                username: username,
                password: password,
            })
            .then(response => {
                let token = response.data.access;
                console.log(token);
                let decode = jwt_decode(token);
                let exp = decode.exp;
                let options = {
                    path: '/',
                    maxAge: exp,
                };
                setToken(token);
                props.setCookie('access', token, options);
                setLoading(false);
                window.location = '/'
            })
            .catch(response => {
                setLoading(false);
                setNotify({open:true, message:'Не верные логин или пароль', type: 'error'});
            });
  };

  return (
    <div>
        <Grid container component="main" className={classes.root}>
      <Grid item xs={false} md={7} className={classes.image} />
      <Grid item xs={12} sm={12} md={5} component={Paper} elevation={6} square>
        <div className={classes.paper}>
          <Avatar className={classes.avatar}
                  src="/logo.png"
                  variant="square"
          />
          <Typography component="h1" variant="h5">
            Войти
          </Typography>
          <form className={classes.form} onSubmit={authenticate} method="POST">
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="username"
              label="Логин"
              name="username"
              autoComplete="username"
              autoFocus
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="password"
              label="Пароль"
              type="password"
              id="password"
              autoComplete="current-password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <FormControlLabel
              control={
                <Checkbox value="remember" color="primary"
                          checked={remember}
                          onChange={(e) => setRemember(e.target.checked)}
                />
              }
              label="Запомнить меня"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Войти
            </Button>
            <Grid container>
              <Grid item xs>
                <Link href="#" variant="body2" onClick={(e) => setResetOpen(true)}>
                  {"Забыли пароль?"}
                </Link>
              </Grid>
              <Grid item>
                <Link href="/register/" variant="body2">
                  {"Нет аккаунта? Зарегистрироваться"}
                </Link>
              </Grid>
            </Grid>
          </form>
        </div>
      </Grid>
      <AlertNotification notify={notify} setNotify={setNotify}/>
      <Dialog open={resetOpen} onClose={(e) => setResetOpen(false)} aria-labelledby="form-dialog-title">
        <DialogTitle id="form-dialog-title">Сбросить пароль</DialogTitle>
        <DialogContent>
          <DialogContentText>
            На указанную почту придет ссылка для перехода на страницу со сменой пароля.
          </DialogContentText>
          <TextField
            autoFocus
            margin="dense"
            id="name"
            label="Электронная почта"
            type="email"
            fullWidth
            name="reset_email"
            value={resetEmail}
            required
            onChange={(e) => setResetEmail(e.target.value)}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={(e) => setResetOpen(false)} color="primary">
            Отмена
          </Button>
          <Button onClick={(e) => setResetOpen(false)} color="primary">
            Сбросить
          </Button>
        </DialogActions>
      </Dialog>
        <Loading loading={loading} />
    </Grid>
    </div>
  );
}