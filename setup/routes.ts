import { defineRoutesSetup } from '@slidev/types'

export default defineRoutesSetup((routes) => {
  return [
    ...routes,
    {
      path: '/home',
      component: () => import('../pages/Home.vue'),
    },
  ]
})