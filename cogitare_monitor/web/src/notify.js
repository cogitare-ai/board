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

    showError: function (title, message, callback) {
        var cfg = config

        if (callback) {
            cfg = Object.assign({}, config)
            cfg.onclick = callback
        }
        toastr.error(message, title, cfg)
    },

    showInfo: function (title, message, callback) {
        var cfg = config

        if (callback) {
            cfg = Object.assign({}, config)
            cfg.onclick = callback
        }
        toastr.info(message, title, cfg)
    }
}
