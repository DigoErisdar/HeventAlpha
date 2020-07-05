import React from 'react';
import Snackbar from "@material-ui/core/Snackbar";
import MuiAlert from '@material-ui/lab/Alert';

function Alert(props) {
  return <MuiAlert elevation={2} variant="standard" {...props} closeText="Закрыть"/>;
}


export default function AlertNotification(props){

    const handleClose = () => {
      props.setNotify({open:false, message:'', type: 'success'})
    };
    return (
        <Snackbar open={props.notify.open} autoHideDuration={6000} onClose={handleClose}>
          <Alert onClose={handleClose} severity={props.notify.type}>
              {props.notify.message}
          </Alert>
        </Snackbar>
    )
}