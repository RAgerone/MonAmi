import React, { Component } from 'react';

class AssistantItem extends React.Component {
  render(){
    return(
      <li className="AssistantItem">
      // This is an individual Assistant component to display on our Assistants List
      {this.props.assistant}
      </li >
    )
  }
}

export default AssistantItem;
