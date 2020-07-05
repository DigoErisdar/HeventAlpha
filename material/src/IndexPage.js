import React from 'react';
import Grid from "@material-ui/core/Grid";
import makeStyles from "@material-ui/core/styles/makeStyles";
import News from "./index/news/News";
import FilterNews from "./index/news/Filter";
import SidebarCard from "./index/SidebarCard";

const useStyles = makeStyles((theme) => ({
  paper: {
    // padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
    // marginBottom: 15,
  },
}));

export default function IndexPage(props) {
    const classes = useStyles();
    return (
        <Grid container spacing={2}>
          <Grid item sm={3} xs={12}>
            <Grid container spacing={2}>
                <Grid item xs={12}>
                    <SidebarCard />
                </Grid>
                <Grid item xs={12}>
                    <SidebarCard />
                </Grid>
            </Grid>
          </Grid>
          <Grid item sm={6} xs={12}>
            <Grid container spacing={2}>
                <Grid item xs={12}>
                    <News />
                </Grid>
                <Grid item xs={12}>
                    <News />
                </Grid>
            </Grid>
          </Grid>
          <Grid item sm={3} xs={12}>
            <Grid container spacing={2}>
                <Grid item xs={12}>
                    <FilterNews />
                </Grid>
            </Grid>
          </Grid>
        </Grid>
    )
}