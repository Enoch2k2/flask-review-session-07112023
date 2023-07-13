import React from 'react'

const Errors = ({ errors }) => {
  const errorLi = errors.map((err, idx) => <li key={idx}>{err}</li>)
  const displayErrors = <ul>{errorLi}</ul>
  return (
    <>
      { errors.length > 0 ? displayErrors : null }
    </>
  )
}

export default Errors