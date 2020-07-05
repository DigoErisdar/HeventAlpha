import React, {useEffect, useState} from 'react';
import PageBreadcrumbs, {getNavigation} from "../../helper/Breadcrumbs";
import Grid from "@material-ui/core/Grid";
import ProfileLeftNav from "./ProfileNavigation";
import makeStyles from "@material-ui/core/styles/makeStyles";
import AccountProfile from "./pages/AccountProfile";
import SidebarCard from "../../index/SidebarCard";

const useStyles = makeStyles((theme) => ({
  control: {
    padding: theme.spacing(2),
  },
}));

export default function ProfilePage({cookie, setPageTitle}) {
  const classes = useStyles();
  const [page, setPage] = useState('account');

  const getPage = () => {
      switch (page) {
          case 'account': return <AccountProfile cookie={cookie} />;
          case 'privates': return "privates";
          case 'chars': return 'chars';
          default:
              return 'Страница не найдена'
      }
  };

  const getPageTitle = () => {
      switch (page) {
          case 'account': return 'Настройки аккаунта';
          case 'profile': return 'Настройки профиля';
          case 'private': return 'Настройки приватности';
      }
  };

  useEffect(() => {
      setPageTitle('Настройки')
  }, [setPageTitle]);

    return <>
            <Grid container className={classes.root} spacing={2}>
                <Grid item xs={12}>
                    <PageBreadcrumbs navigation={getNavigation('profile')} />
                </Grid>
                <Grid item xs={12}>
                    <Grid container spacing={3}>
                        <Grid item xs={12} sm={4}>
                            <SidebarCard header={'Настройки'}
                                         component={<ProfileLeftNav selected={page} setPage={setPage} />}/>
                          </Grid>
                          <Grid item xs={12} sm={8}>
                            <SidebarCard header={getPageTitle()} component={getPage()}/>
                          </Grid>
                    </Grid>
                </Grid>
            </Grid>
        </>
}