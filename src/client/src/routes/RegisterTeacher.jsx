import React from "react";
import Card from "@material-ui/core/Card";
import { Form } from "react-bootstrap";
import { Button } from "@material-ui/core/";
import TextField from "@material-ui/core/TextField";
import CardHeader from "@material-ui/core/CardHeader";
import CardContent from "@material-ui/core/CardContent";

export default class Register extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      teacher_email: "",
      teacher_password: "",
      teacher_name: "",
      teacher_gender: "",
      teacher_department: "",
      teacher_location: "",
      teacher_phone_number: ""
    };
  }

  handleChange(e) {
    e.preventDefault();
    console.log(this.state);
    this.setState({
      [e.target.name]: e.target.value
    });
  }

  handleSubmit(e) {
    e.preventDefault();
    console.log(this.state);
    // axios.post("http://localhost:5000/signupTeacher",{
    //     email: this.state.email,
    //     password: this.state.password,
    //     name: this.state.name,
    // })
    // .then(a => {
    //     console.log(a)
    //     if(a.data["Status"] === false){
    //         alert("Email already present. Please login")
    //         this.props.history.push("/login")

    //     }
    //     else{
    //         console.log(a.data)
    //         localStorage.setItem("data", JSON.stringify(a.data))
    //         this.props.history.push("/login")
    //     }
    // })
    // .catch(err => console.log(err));
  }

  render() {
    return (
      <div className="row justify-content-center">
        <Card className="m-5 p-5">
          <CardHeader
            style={{ backgroundColor: "#313F9F" }}
            className="p-2 pl-5 pr-5 text-white rounded-pill text-center"
            title="Register Now"
          />
          <br />
          <CardContent>
            <Form>
              <TextField
                name="teacher_name"
                onChange={e => this.handleChange(e)}
                type="text"
                label="Enter Your Full Name"
              />
              <br />
              <TextField
                className="mt-2"
                name="teacher_email"
                onChange={e => this.handleChange(e)}
                type="email"
                label="Enter Email"
              />
              <br />
              <TextField
                className="mt-2"
                name="teacher_password"
                onChange={e => this.handleChange(e)}
                type="password"
                label="Enter Password"
              />
              <br />
              <TextField
                name="teacher_gender"
                onChange={e => this.handleChange(e)}
                type="text"
                label="Enter Gender"
              />
              <br />
              <TextField
                name="teacher_department"
                onChange={e => this.handleChange(e)}
                type="text"
                label="Enter Department"
              />
              <br />
              <TextField
                name="teacher_location"
                onChange={e => this.handleChange(e)}
                type="text"
                label="Enter Location"
              />
              <br />
              <TextField
                className="mt-2"
                name="teacher_phone_number"
                onChange={e => this.handleChange(e)}
                type="number"
                label="Enter Phone Number"
              />
              <br />
              <Button
                className="mt-4"
                variant="contained"
                color="primary"
                type="submit"
              >
                Submit
              </Button>
            </Form>
          </CardContent>
        </Card>
      </div>
    );
  }
}
