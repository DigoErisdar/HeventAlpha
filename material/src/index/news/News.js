import React from 'react';
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardMedia from "@material-ui/core/CardMedia";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import CardActions from "@material-ui/core/CardActions";
import makeStyles from "@material-ui/core/styles/makeStyles";
import CardHeader from "@material-ui/core/CardHeader";
import Avatar from "@material-ui/core/Avatar";
import IconButton from "@material-ui/core/IconButton";
import MoreVertIcon from '@material-ui/icons/MoreVert';
import FavoriteIcon from '@material-ui/icons/Favorite';
import ShareIcon from '@material-ui/icons/Share'
import Chip from "@material-ui/core/Chip";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import {Favorite, FavoriteBorder} from "@material-ui/icons";
import Checkbox from "@material-ui/core/Checkbox";

const useStyles = makeStyles({
  tags: {
      marginLeft: 'auto',
  },
  tag: {
      margin: 1,
  }
});

export default function News({news}) {
    const classes = useStyles();

    return (
        <>
         <Card className={classes.root}>
             <CardHeader
                avatar={
                  <Avatar className={classes.avatar} />
                }
                action={
                  <IconButton >
                    <MoreVertIcon />
                  </IconButton>
                }
                title="~Digo~"
                subheader="Сегодня"

              />
          <CardActionArea>
            <CardMedia
              component="img"
              alt="Саргас. Расписание от 25.06.20"
              height="140"
              image="https://sun9-68.userapi.com/LNZSa_dOq15PIPafIBLn2j2TXLylDeO7M0NpBQ/nOCBmki1sN4.jpg"
              title="Саргас. Расписание от 25.06.20"
            />
            <CardContent>
              <Typography gutterBottom variant="h5" component="h2">
                Саргас. Расписание от 25.06.20
              </Typography>
              <Typography variant="body2" color="textSecondary" component="p">
                Приветствую, дорогие подписчики. На сервере середина 85й недели, а значит самое время посмотреть что и как
                Хоть статья и поздняя, но результаты должны быть в результатах
                Пройдемся по ставочкам… Погнали
              </Typography>
            </CardContent>
          </CardActionArea>
          <CardActions disableSpacing style={{paddingLeft: 15, paddingRight: 15}}>
                <FormControlLabel
                control={<Checkbox icon={<FavoriteBorder />} checkedIcon={<Favorite />} name="like" />}
                label={'15'}

              />
              <div className={classes.tags}>
                  <Chip color="primary" size="small" label={"ГВГ"} className={classes.tag}/>
                  <Chip color="primary" size="small" label={"Саргас"} className={classes.tag}/>
                  <Chip color="primary" size="small" label={"Арена 3х3"} className={classes.tag}/>
                  <Chip color="primary" size="small" label={"Тег"} className={classes.tag}/>
              </div>
          </CardActions>
        </Card>
        </>
    )
}