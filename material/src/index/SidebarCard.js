import React from "react";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import makeStyles from "@material-ui/core/styles/makeStyles";
import CardContent from "@material-ui/core/CardContent";
import CardActions from "@material-ui/core/CardActions";

const useStyles = makeStyles((theme) => ({
    header:{
        textAlign:'center',
    }
}));


export default function SidebarCard(props) {
    const classes = useStyles();
    return (
        <Card>
            <CardHeader
                title={props.header}
                subheader={props.subheader}
                className={classes.header}
                />
            <CardContent>
                {props.component}
            </CardContent>
            <CardActions>
            </CardActions>
        </Card>
    )
}