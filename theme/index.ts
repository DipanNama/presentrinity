// theme/index.ts

import Button from '../components/Button.vue';  // Import your global component

export default {
  enhanceApp({ app }) {
    app.component('Button', Button);  // Register the component globally
  },
};
