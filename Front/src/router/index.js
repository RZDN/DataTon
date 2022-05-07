import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SupplierView from "@/views/SupplierView";
import StatisticsView from "@/views/StatisticsView";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: StatisticsView
  },
  {
    path: '/supplier',
    name: 'supplier',
    component: SupplierView
  },
  {
    path: '/statistics',
    name: 'statistics',
    component: StatisticsView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
