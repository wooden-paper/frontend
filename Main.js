import React, {Component} from 'react';

function buildTable(arr){
  const rows = arr.map((row,i) => { 
      return <tr style={{backgroundColor: i%2 ? '#F0FFF2':'white'}}  key={i}>
                <td>{row["name"]}</td><td>{row["valid"] ? <div style={{backgroundColor: "#aaccaa"}}>✓</div>:<div style={{backgroundColor: "#ccaaaa"}}>✗</div> }</td><td><a href={'http://localhost:5000/api/get/' + row["name"]} download>Click to download</a></td>
             </tr> 
  })
  return <table className="center"><tbody>{rows}</tbody></table>
}

class Main extends Component {
  constructor(props) {
    super(props);
    this.state = {
      from: "",
      to: "",
      results: []
    }

  }
  search = () => {
      fetch(`http://localhost:5000/api/validate?from=${encodeURIComponent(this.state.from)}&to=${encodeURIComponent(this.state.to)}`)
          .then(r => r.json())
          .then(r => this.setState({"results": r}))
  }
  handleFromChangeValue = event => {console.log(event.target.value);this.setState({from: event.target.value}, () => console.log(this.state.from))};
  handleToChangeValue = event => {console.log(event.target.value);this.setState({to: event.target.value}, () => console.log(this.state.from))};
  handleKeyPress = event => {
    if (event.key === 'Enter' || event.keyCode == 13) {
      this.search()
    }
  }

  render() {
    return (
        <div className="main" key={"main"}>
          
          <h3>From</h3>
          <div className="center"><input key={"from"} onKeyDown={(e) => this.handleKeyPress(e)} onChange={(e) => this.handleFromChangeValue(e)}/></div>
          
          <h3>To</h3>
          <div className="center"><input key={"to"} onKeyDown={(e) => this.handleKeyPress(e)} onChange={(e) => this.handleToChangeValue(e)}/></div>
          <div className="center"><button onClick={this.props.search}>Search</button></div>
          {buildTable(this.state.results)}
        </div>
    );
  }
}

export default Main;
