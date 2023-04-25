import { get, getAll } from './utils/getElement.js'

// Show / hide navlinks
const navBtn = get('.nav-btn')
const linksContainer = get('.links-container')
const navLinks = get('.navlinks')

navBtn.addEventListener('click', (e) => {
  // get height of elements
  const linksContainerHeight = linksContainer.getBoundingClientRect().height
  const linksHeight = navLinks.getBoundingClientRect().height

  if (linksContainerHeight === 0) {
    linksContainer.style.height = `${linksHeight}px`
  } else {
    linksContainer.style.height = 0
  }
  e.currentTarget.classList.toggle('rotate')
})
