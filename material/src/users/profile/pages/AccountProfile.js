import React, {useEffect, useState} from 'react';
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import Grid from "@material-ui/core/Grid";
import Button from "@material-ui/core/Button";
import axios from 'axios';
import {setToken} from "../../../helper/api";
import Loading from "../../../helper/loading";
import AlertNotification from "../../../helper/Alert";
import DialogTitle from "@material-ui/core/DialogTitle";
import DialogContent from "@material-ui/core/DialogContent";
import DialogActions from "@material-ui/core/DialogActions";
import Dialog from "@material-ui/core/Dialog";
import FormControl from "@material-ui/core/FormControl";
import InputLabel from "@material-ui/core/InputLabel";
import Select from "@material-ui/core/Select";
import MenuItem from "@material-ui/core/MenuItem";
import {DatePicker} from "@material-ui/pickers";

export default function AccountProfile({cookie}){
    const [loading, setLoading] = useState(false);
    const [notify, setNotify] = useState({open:false, message:'', type: 'success'});
    const [dialogOpen, setDialogOpen] = useState(false);
    const [errors, setErrors] = useState({});

    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');

    const [oldPassword, setOldPassword] = useState(null);
    const [newPassword, setNewPassword] = useState(null);

    const [sex, setSex] = useState('');
    const [name, setName] = useState('');
    const [dateBirthday, setDateBirthday] = useState(null);


    useEffect(()=> {
        setToken(cookie.access);
        setLoading(true);
        axios.get(`/api/users/current/`)
            .then(response => {
                let data = response.data;
                setUsername(data.username);
                setEmail(data.email);

                setSex(data.profile.sex);
                setName(data.profile.name);
                setDateBirthday(data.profile.date_brithday);

                setLoading(false);
            })
            .catch(error => {
                console.error(error.response);
                setLoading(false);
            })
    }, [cookie.access]);

    const saveAccount = (event) => {
        event.preventDefault();
        setLoading(true);
        axios.put('/api/users/current/',{
            username:username,
            email:email,
            profile: {
                name: name,
                sex: sex,
                date_birthday: dateBirthday,
            },
        })
            .then(response => {
                console.log(response);
                setLoading(false);
                setNotify({open:true, message:'Сохранения изменены', type: 'success'})
            })
            .catch(error => {
                setLoading(false);
                console.error(error.response);
            })
    };

    const changePassword = (event) => {
        event.preventDefault();
        setLoading(true);
        axios.put('/api/users/current/change_password/', {
                old_password: oldPassword,
                new_password: newPassword,
            })
            .then(response => {
                setDialogOpen(false);
                setLoading(false);
                setNotify({open:true, message:'Пароль изменен', type: 'success'})
            }).catch(error => {
                setLoading(false);
                setErrors(error.response.data);
            })
    };

    const dialog = (
      <Dialog open={dialogOpen} onClose={(e) => setDialogOpen(false)} aria-labelledby="form-dialog-title">
        <DialogTitle id="form-dialog-title">Сменить пароль</DialogTitle>
        <form method={"POST"} onSubmit={changePassword}>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            id="old_password"
            label="Старый пароль"
            type="password"
            fullWidth
            name="old_password"
            value={oldPassword}
            required
            error={!!errors.old_password}
            helperText={errors.old_password ? errors.old_password : null}
            onChange={(e) => setOldPassword(e.target.value)}
            variant={"standard"}
          />
          <TextField
            margin="dense"
            id="new_password"
            label="Новый пароль"
            type="password"
            fullWidth
            name="new_password"
            value={newPassword}
            required
            error={!!errors.new_password}
            helperText={errors.new_password ? errors.new_password : null}
            onChange={(e) => setNewPassword(e.target.value)}
            variant={"standard"}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={(e) => setDialogOpen(false)} color="primary">
            Закрыть
          </Button>
          <Button type={"submit"} color="primary">
            Сменить пароль
          </Button>
        </DialogActions>
        </form>
      </Dialog>
    );

    return (
        <>
            <form method={"POST"} onSubmit={saveAccount}>
                <Grid container spacing={2}>
                    <Grid item xs={12} md={6}>
                        <TextField
                            variant="outlined"
                            required
                            fullWidth
                            id="username"
                            label="Логин"
                            name="username"
                            autoComplete="username"
                            autoFocus
                            error={!!errors.username}
                            helperText={errors.username ? errors.username : null}
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={12} md={6}>
                        <TextField
                            variant="outlined"
                            required
                            fullWidth
                            id="email"
                            label="Электронная почта"
                            name="email"
                            autoComplete="email"
                            autoFocus
                            value={email}
                            error={!!errors.email}
                            helperText={errors.email ? errors.email : null}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={12} md={6}>
                        <TextField
                            variant="outlined"
                            fullWidth
                            id="name"
                            label="Имя"
                            name="email"
                            autoComplete="email"
                            autoFocus
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={12} md={6}>
                        <FormControl fullWidth variant={"standard"} margin={"normal"}>
                            <InputLabel id="sex-label">Пол</InputLabel>
                            <Select
                              labelId="sex-label"
                              id="demo-customized-select"
                              value={sex}
                              onChange={(e)=> setSex(e.target.value)}
                            >
                              <MenuItem value="">Не выбрано</MenuItem>
                              <MenuItem value={"male"}>Мужской</MenuItem>
                              <MenuItem value={"female"}>Женский</MenuItem>
                            </Select>
                          </FormControl>
                    </Grid>
                    <Grid item xs={12} md={6}>
                        <DatePicker
                            autoOk
                            label="Дата рождения"
                            clearable
                            format="dd MMMM"
                            value={dateBirthday}
                            onChange={setDateBirthday}
                            okLabel={'ОК'}
                            cancelLabel={"Отменить"}
                            clearLabel={'Сбросить'}
                            helperText={"Год нигде не учитывается"}
                            fullWidth
                          />
                    </Grid>
                    <Grid item xs={12} md={6} >
                        <Button color={"primary"} variant={"contained"} fullWidth type={"submit"}>
                            Сохранить
                        </Button>
                    </Grid>
                    <Grid item xs={12} md={6}>
                        <Button color={"primary"} variant={"contained"} fullWidth
                                onClick={() => setDialogOpen(true)}>
                            Сменить пароль
                        </Button>
                    </Grid>
                </Grid>
            </form>
        <Loading loading={loading} />
        <AlertNotification notify={notify} setNotify={setNotify}/>
        {dialog}
        </>
    )
}