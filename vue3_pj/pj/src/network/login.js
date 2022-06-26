import axios from 'axios'

export const Login = (user) =>{
  // 进行登录， 登录成功保存token
  const requests = axios.post(
    'api/login/',user
  ).then(res=>{
    // 缓存token和用户名
    localStorage.setItem('token',res.data.token)
    localStorage.setItem('username', user.username)
    return true
  }
  ).catch(err=>{
    return  err.response.data
    
  })

  return requests
}
