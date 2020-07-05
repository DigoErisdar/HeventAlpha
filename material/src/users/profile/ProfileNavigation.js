import React from 'react';
import List from "@material-ui/core/List";
import ListSubheader from "@material-ui/core/ListSubheader";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import makeStyles from "@material-ui/core/styles/makeStyles";

const useStyles = makeStyles((theme) => ({
  nested: {
    paddingLeft: theme.spacing(4),
  },
}));

export default function ProfileLeftNav({ selected = '', setPage}) {
    const classes = useStyles();
    return (
        <List
          component="nav"
          aria-labelledby="nested-list-subheader"
          subheader={
            <ListSubheader component="div" id="nested-list-subheader">
              Настройки
            </ListSubheader>
          }
        >
          <ListItem button key='account' selected={selected === 'account'} onClick={() => setPage('account')}>
            <ListItemText primary="Аккаунт" />
          </ListItem>
          <ListItem button key='chars' selected={selected === 'chars'} onClick={() => setPage('chars')}>
            <ListItemText primary="Персонажи" />
          </ListItem>
        </List>
    )
}