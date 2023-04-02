// import request from '../utils/request'
const request = require('../utils/request').default;
// const baseURL = 'http://localhost:8090'
// let access_token = '24.8de2691abb045664235e0e352638cd02.2592000.1683021509.282335-31923322'

export function check(params) {
    return request({
        url: '/auth/face',
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        data: params
    });
}