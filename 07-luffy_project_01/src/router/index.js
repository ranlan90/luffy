import Vue from 'vue'
import Router from 'vue-router'
// @ 绝对路径 检索到 .....src/

// 如果我们Router当做局部模块使用 一定要Vue.use(Router)
// 以后在组件中  可以通过this.$router  获取Router实例化对象
// 路由信息对象 this.$routes
import Home from '@/components/Home/Home'
import Course from '@/components/Course/Course'
import LightCourse from '@/components/LightCourse/LightCourse'
import Micro from '@/components/Micro/Micro'
import CourseDetail from '@/components/Course/CourseDetail'
import Login from '@/components/Login/Login'
import Register from '@/components/Register/Register'
import Cart from '@/components/Cart/Cart'
import Account from '@/components/Cart/Account'
import MyOrder from '@/components/Order/MyOrder'
import PaySuccess from '@/components/Order/PaySuccess'

Vue.use(Router)

// 配置路由规则
export default new Router({
   linkActiveClass:'is-active',
   mode: 'history',//改成history模式
  routes: [
    {
      path: '/',
      redirect:'/home'
      // component: HelloWorld
    },
    {
    	path:"/home",
    	name:'Home',
    	component:Home
    },
    {
    	path:"/courses",
    	name:'Course',
    	component:Course
    },
    {
    	path:"/light-course",
    	name:'LightCourse',
    	component:LightCourse
    },
    {
    	path:"/micro",
    	name:'Micro',
    	component:Micro
    },
    // 课程详情
    {
      path:"/course/detail/web/:detailId",
      name:'course.detail',
      component:CourseDetail
    },
    {
      path:'/login',
      name:'Login',
      component:Login,
      meta:{
        hide:true
      }
    },
    {
      path:'/register',
      name:'Register',
      component:Register,
      meta:{
        hide:true
      }
    },
    // 购物车的页面
    {
      path:"/purchase/shopping_cart",
      name:'purchase.shop',
      component:Cart,
      meta: {
        requiresAuth: true
      }
    },
    {
     path:'/buy',
      name:'account',
      component:Account,
      meta: {
        requiresAuth: true
      }
    },
    {
      path:'/my/order',
      name:'my_order',
      component:MyOrder,
      meta: {
        requiresAuth: true
      }
    },
    {
      path:'/order/pay_success',
      name:'pay_success',
      component:PaySuccess,
      meta: {
        requiresAuth: true
      }
    }
  ]
})
