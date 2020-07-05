import axios from 'axios';

export function setToken(token='') {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  axios.defaults.headers.post['Content-Type'] = 'application/json; charset=utf-8';
  axios.defaults.headers.common['Access-Control-Allow-Headers'] = 'Authorization';
}

export default axios;