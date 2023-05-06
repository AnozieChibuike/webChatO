import { get } from './getElement.js'

const loading = get('.loading')

const showLoading = () => {
  loading.classList.add('show-loading')
}

export default showLoading
