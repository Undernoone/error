import axios from '@/utils/request.js'

const api = {
  createApi: '/myapp/index/shop_car/create',
  queryListApi: '/myapp/index/shop_car/query_list',
  queryOneApi: '/myapp/index/shop_car/query_one',
  updateApi: '/myapp/index/shop_car/update',
  deleteApi: '/myapp/index/shop_car/delete'
}

export const createShopCarApi = function (data) {
  return axios({
    url: api.createApi,
    method: 'post',
    data: data
  })
}

export const queryShopCarListApi = function (params) {
  return axios({
    url: api.queryListApi,
    method: 'get',
    params: params
  })
}