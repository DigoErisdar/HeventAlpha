import React, {useState} from 'react';
import makeStyles from "@material-ui/core/styles/makeStyles";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";
import axios from "axios";
import jwt_decode from "jwt-decode";
import Link from "@material-ui/core/Link";
import Avatar from "@material-ui/core/Avatar";
import CircularProgress from "@material-ui/core/CircularProgress";
import Backdrop from "@material-ui/core/Backdrop";


const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(1),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      },
      avatar: {
        margin: theme.spacing(1),
      },
      form: {
        width: '100%', // Fix IE 11 issue.
        marginTop: theme.spacing(3),
      },
      submit: {
        margin: theme.spacing(3, 0, 2),
      },
      backdrop: {
        zIndex: theme.zIndex.drawer + 1,
        color: '#fff',
      },
    }));


export default function RegisterPage(props) {
    const classes = useStyles();

    const [username, setUsername] = useState('');
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const [errors, setErrors] = useState({});
    const [loading, setLoading] = useState(false);

    const clear_errors = (name) => {
        if (errors) {
            const copyErrors = {...errors};
            delete copyErrors[name];
            setErrors(copyErrors)
        }
    };

    const register = (event) => {
        event.preventDefault();
        setLoading(true);
        axios.post('/api/users/register/', {
            username: username,
            password: password,
            email: email,
        })
            .then(response => {
                let token = response.data.access;
                let decode = jwt_decode(token);
                let exp = decode.exp;
                let options = {
                    path: '/',
                    maxAge: exp,
                };
                props.setCookie('access', token, options);
                axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
                setLoading(false);
                window.location = '/';
            })
            .catch(error => {
                setLoading(false);
                if (error.response.data) {
                    setErrors(error.response.data);
                }
            });
    };


    return (
        <Container component="main" maxWidth="xs">
            <div className={classes.paper}>
                <Avatar className={classes.avatar}
                        src="/logo.png"
                        variant="square"
                />
                <Typography component="h1" variant="h5">
                    Регистрация
                </Typography>
                <form className={classes.form} onSubmit={register}>
                    <Grid container spacing={2}>
                        <Grid item xs={12}>
                            <TextField
                                variant="outlined"
                                required
                                error={!!errors.username}
                                fullWidth
                                id="username"
                                label="Логин"
                                name="username"
                                autoComplete="username"
                                autoFocus
                                value={username}
                                onChange={(e) => {
                                    setUsername(e.target.value);
                                    clear_errors(e.target.name);
                                }}
                                helperText={!!errors.username ? errors.username : null}
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                variant="outlined"
                                required
                                error={!!errors.email}
                                fullWidth
                                id="email"
                                label="Электронная почта"
                                name="email"
                                autoComplete="email"
                                value={email}
                                onChange={(e) => {
                                    setEmail(e.target.value);
                                    clear_errors(e.target.name);
                                }}
                                helperText={!!errors.email ? errors.email : "Необходима для восстановления пароля"}
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                variant="outlined"
                                required
                                error={!!errors.password}
                                fullWidth
                                id="password"
                                label="Пароль"
                                name="password"
                                autoComplete="password"
                                value={password}
                                type="password"
                                onChange={(e) => {
                                    setPassword(e.target.value);
                                    clear_errors(e.target.name);
                                }}
                                helperText={!!errors.password ? errors.password : null}
                            />
                        </Grid>
                    </Grid>
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                        className={classes.submit}
                    >
                        Зарегистрироваться
                    </Button>
                    <Grid container justify="flex-end">
                        <Grid item>
                            <Link href="/login/" variant="body2">
                                Уже есть аккаунт? Войти
                            </Link>
                        </Grid>
                    </Grid>
                </form>
                <Backdrop open={loading} className={classes.backdrop}>
                  <CircularProgress color="inherit" />
                </Backdrop>
            </div>
        </Container>
    );
}