import React from "react";
import CardHeader from '@material-ui/core/CardHeader';
import Card from '@material-ui/core/Card';
import {Form} from "react-bootstrap";
import {Button} from "@material-ui/core/";
import TextField from '@material-ui/core/TextField';
class Login extends React.Component{
  constructor(props){
      super(props);
      this.state = {
          email: "",
          password: ""
      }
  }

  handleChange(e){
    e.preventDefault();
    console.log(this.state)
      this.setState({
          [e.target.name]: e.target.value
      })
  }

  handleSubmit(e){
      e.preventDefault();
      console.log(this.state)
      // axios.post('http://localhost:5000/login',{
      //     email: this.state.email,
      //     password: this.state.password
      // })
      // .then(a => {
      //     console.log(a)
      //     if(a.data["User Login"] === false){
      //         alert("Invalid email or password.")
      //     }
      //     else{
      //         console.log(a.data)
      //         localStorage.setItem('data', JSON.stringify(a.data))
      //         this.props.history.push("/dash")
      //     }
      // })
      // .catch(err => console.log(err));
  }
render(){
  return (
    <div className="row justify-content-center">
      <Card className="m-5 p-5">
      <CardHeader
        title="Login"
        style={{backgroundColor:"#313F9F"}}
        className="p-2 text-white rounded-pill text-center"
      />
      <br/>
      <Form>
        <TextField name="email" onChange={e => this.handleChange(e)} type="email" label="Enter Email" />
        <br/>
        <TextField className="mt-2" name="password" onChange={e => this.handleChange(e)} type="password" label="Enter Password" />
        <br/>
        <Button className="mt-4" variant="contained" color="primary" type="submit">
          Submit
        </Button>
      </Form>
      </Card>
    </div>
  );
}
};

export default Login;
