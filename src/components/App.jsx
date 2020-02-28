import React from 'react';
import { Link } from 'react-router-dom';

export default class AppWrapper extends React.Component {
  render() {
    return (
      <div className='app-container'>
        <Link to={'/'}>Home</Link>
        <Link to={'/play'}>Play</Link>
        {this.props.children}
      </div>
    )
  }
}