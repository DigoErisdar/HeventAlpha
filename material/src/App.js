import React, {useState} from 'react';
import Header from './Header';
import Footer from "./Footer";
import makeStyles from "@material-ui/core/styles/makeStyles";
import CssBaseline from "@material-ui/core/CssBaseline";
import LoginPage from "./users/login/LoginPage";
import {Route, Switch} from 'react-router-dom';
import RegisterPage from "./users/register/Register";
import { useCookies } from "react-cookie";
import NoMatchPage from "./helper/404";
import IndexPage from "./IndexPage";
import ProfilePage from "./users/profile/ProfilePage";

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    flexDirection: 'column',
    minHeight: '100vh',
  },
  footer: {
    padding: theme.spacing(3, 2),
    marginTop: 'auto',
    backgroundColor:
      theme.palette.type === 'light' ? theme.palette.grey[200] : theme.palette.grey[800],
  },
}));


export default function App() {
  const classes = useStyles();
  const [cookie, setCookie, removeCookie] = useCookies(['access']);
  const [pageTitle, setPageTitle] = useState('Главная');
  const auth = !!cookie.access;

  return (
    <div className={classes.root}>
       <CssBaseline />
        <Header isAuth={auth} cookie={cookie} removeCookie={removeCookie} title={pageTitle} />
        <div style={{padding:16}}>
              <Switch>
                <Route exact path={'/'} component={() => <IndexPage/> } />
                <Route exact path='/login/'
                       component={() => <LoginPage setCookie={setCookie} />} />
                <Route exact path='/register/'
                       component={() => <RegisterPage setCookie={setCookie} />} />
                <Route exact path='/profile/' component={() => <ProfilePage cookie={cookie} setPageTitle={setPageTitle} />} />
                <Route component={() => <NoMatchPage />} />
              </Switch>
          </div>
        <Footer />
    </div>
  );
}
