import axios from 'axios';

let base = 'http://127.0.0.1:8000';

//获取产品线
export const queryProductlines = params => { return axios.get(`${base}/productlines/`, params).then(res => res.data); };


//获取故障类型

export const queryTroubles = params => { return axios.get(`${base}/troubles/`, params).then(res => res.data); };


export const getProblemList = params => { return axios.get(`${base}/api/troubles/`, { params: params }); };

export const getUserListPage = params => { return axios.get(`${base}/pcinfos/`, { params: params }); };

export const removeUser = params => { return axios.get(`${base}/user/remove`, { params: params }); };

export const batchRemoveUser = params => { return axios.get(`${base}/user/batchremove`, { params: params }); };

export const editProblem = params => { return axios.get(`${base}/user/edit`, { params: params }); };

export const addUser = params => { return axios.get(`${base}/user/add`, { params: params }); };




