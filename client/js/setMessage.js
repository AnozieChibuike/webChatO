import { get } from './getElement.js'
const message = get('.message')

const setMessage = (text) => {
  message.textContent = text
  message.classList.add('active')
  setTimeout(() => {
    message.textContent = ''
    message.classList.remove('active')
  }, 2000)
}

export default setMessage
