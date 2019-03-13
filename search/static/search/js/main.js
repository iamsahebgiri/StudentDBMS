
const app =new Vue({
    el: '#app',
    data: {
        message: 'Add Student Details',
        rg: Math.floor(Math.random()*16777215).toString(16)
    },
    delimiters: ['[[',']]']
})