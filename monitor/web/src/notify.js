import toastr from 'toastr'
import 'toastr/build/toastr.css'

const config = {
    timeout: 3000,
    preventDuplicates: true,
    closeButton: true,
    progressBar: true,
    newestOnTop: true
}

export default {

    showError: function (title, message) {
        toastr.error(message, title, config)
    },

    showInfo: function (title, message) {
        toastr.info(message, title, config)
    }
}
