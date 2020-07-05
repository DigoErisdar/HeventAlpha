import React from "react";
import Checkbox from "@material-ui/core/Checkbox";
import ListItemSecondaryAction from "@material-ui/core/ListItemSecondaryAction";
import ListItem from "@material-ui/core/ListItem";
import List from "@material-ui/core/List";
import ListItemText from "@material-ui/core/ListItemText";
import makeStyles from "@material-ui/core/styles/makeStyles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CardHeader from "@material-ui/core/CardHeader";
import CardActions from "@material-ui/core/CardActions";
import Button from "@material-ui/core/Button";
import ListSubheader from "@material-ui/core/ListSubheader";

const useStyles = makeStyles((theme) => ({
    header:{
        textAlign:'center',
    }
}));


export default function FilterNews(){
  const classes = useStyles();
  const [checked, setChecked] = React.useState([1]);

  const handleToggle = (value) => () => {
    const currentIndex = checked.indexOf(value);
    const newChecked = [...checked];

    if (currentIndex === -1) {
      newChecked.push(value);
    } else {
      newChecked.splice(currentIndex, 1);
    }

    setChecked(newChecked);
  };

  return (
  <Card>
   <CardHeader
    title="Фильтры"
    className={classes.header}
    />
  <CardContent>
    <List
        subheader={
        <ListSubheader component="div" id="nested-list-subheader">
          Фильтр по серверу
        </ListSubheader>
        }>
      <ListItem button>
        <ListItemText primary={`Титан`} />
        <ListItemSecondaryAction>
          <Checkbox
            edge="end"
          />
        </ListItemSecondaryAction>
      </ListItem>
      <ListItem button>
        <ListItemText primary={`Саргас`} />
        <ListItemSecondaryAction>
          <Checkbox
            edge="end"
          />
        </ListItemSecondaryAction>
      </ListItem>
    </List>
    <List
        subheader={
        <ListSubheader component="div" id="nested-list-subheader">
          Фильтр по тегу
        </ListSubheader>
        }>
      <ListItem button>
        <ListItemText primary={`Арена 3х3`} />
        <ListItemSecondaryAction>
          <Checkbox
            edge="end"
          />
        </ListItemSecondaryAction>
      </ListItem>
      <ListItem button>
        <ListItemText primary={`ГВГ`} />
        <ListItemSecondaryAction>
          <Checkbox
            edge="end"
          />
        </ListItemSecondaryAction>
      </ListItem>
    </List>
  </CardContent>
  <CardActions>
    <Button size="medium" variant={"contained"} color="primary" style={{margin:'auto'}}>
      Показать
    </Button>
  </CardActions>
  </Card>
  );
}