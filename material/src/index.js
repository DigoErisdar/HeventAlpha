import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {BrowserRouter} from "react-router-dom";
import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import ruLocale from "date-fns/locale/ru";
import DateFnsUtils from '@date-io/date-fns';
import { CookiesProvider } from 'react-cookie';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import orange from "@material-ui/core/colors/orange";
import red from "@material-ui/core/colors/red";

const theme = createMuiTheme({
  palette: {
    primary: {
      main: orange[900],
    },
    secondary: {
      main: red[700],
    },
  },
});

ReactDOM.render(
  <React.StrictMode>
    <MuiPickersUtilsProvider utils={DateFnsUtils} locale={ruLocale}>
      <CookiesProvider>
          <BrowserRouter>
              <ThemeProvider theme={theme}>
                <App />
              </ThemeProvider>
          </BrowserRouter>
      </CookiesProvider>
    </MuiPickersUtilsProvider>
  </React.StrictMode>,
  document.getElementById('Hevent')
);
