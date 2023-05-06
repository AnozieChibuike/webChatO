import { get } from './getElement.js'
import setMessage from './setMessage.js'
import showLoading from './showLoading.js'

// select elements
const form = get('.form')
const email = get('#email')

// regex
const emailRegex = /^\w+([\\.-]?\w+)*@\w+([\\.-]?\w+)*(\.\w{2,3})+$/

const validateInputs = () => {
  if (email.value === '') {
    setMessage('email is required')
    email.focus()
  } else if (!email.value.match(emailRegex)) {
    setMessage('invalid email')
    email.focus()
  } else {
    setMessage('processing...')
    showLoading()
  }
}

form.addEventListener('submit', (e) => {
  e.preventDefault()
  validateInputs()
})
