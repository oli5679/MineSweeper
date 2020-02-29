import React from 'react';
import { Link } from 'react-router-dom';
import { Container, Divider, Grid, Header, Icon } from 'semantic-ui-react'

export default class AppWrapper extends React.Component {
  render() {
    return (
      <Container>
    {/* Heads up! We apply there some custom styling, you usually will not need it. */}

    <Header as='h2' icon inverted textAlign='center'>
      <Icon name='grid layout' />
      Minesweeper
      <Header.Subheader>
        Do you wanna play some minesweeper to remind you of the good old days?
      </Header.Subheader>
    </Header>
    <Divider />
    <Header as='h2' icon inverted textAlign='center'>
        <Link to={'/'}>Home</Link>
        <Link to={'/play'}>Play</Link>
        {this.props.children}
      </Header>
    </Container>
    )
  }
}