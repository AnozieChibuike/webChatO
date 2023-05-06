import { get } from './getElement.js'
import setMessage from './setMessage.js'

// select elements
const form = get('.form')
const email = get('#email')
const username = get('#username')
const password = get('#password')
const confirmPassword = get('#confirmPassword')

// regex
const emailRegex = /^\w+([\\.-]?\w+)*@\w+([\\.-]?\w+)*(\.\w{2,3})+$/
const FirstCharIsNum = /^[0-9].*$/

const validateInputs = () => {
  // email
  if (email.value === '') {
    setMessage('email is required')
    email.focus()
  } else if (!email.value.match(emailRegex)) {
    setMessage('invalid email')
    email.focus()
  }
  // username
  else if (username.value === '') {
    setMessage('username is required')
    username.focus()
  } else if (username.value.match(FirstCharIsNum)) {
    setMessage('username cannot start with a number')
    username.focus()
  } else if (username.value.length < 4) {
    setMessage('username cannot be less than 4 characters')
    username.focus()
  }
  // password
  else if (password.value === '') {
    setMessage('password is required')
    password.focus()
  } else if (password.value.length < 6) {
    setMessage('password too short')
    password.focus()
  }
  // confirm password
  else if (confirmPassword.value !== password.value) {
    setMessage('passwords do not match')
    confirmPassword.focus()
  } else {
    setMessage('sign up successful')
  }
}

form.addEventListener('submit', (e) => {
  e.preventDefault()
  validateInputs()
})
