import React from "react";
import {
  MDBRow,
  MDBCol,
  MDBCard,
  MDBCardBody,
  MDBIcon,
  MDBBtn,
  MDBInput
} from "mdbreact";

const addProject = () => {
  return alert("Thank You for Your Response. We will contact you Shortly");
  // alert('Project Added');
};

const Contact = () => {
  return (
    <div className="container-fluid row justify-content-center">
      <section className="my-5">
        <h1 className="h1-responsive font-weight-bold text-center text-info my-5">
          <MDBIcon icon="map-marked-alt" /> Contact us
        </h1>
        <MDBRow>
          <MDBCol lg="5" className="lg-0 mb-4">
            <MDBCard>
              <MDBCardBody>
                <div className="form-header rounded-pill pt-1 pb-1 bg-primary accent-1">
                  <h3 className="text-center text-white mt-2">
                    <MDBIcon icon="envelope" /> Write to us:
                  </h3>
                </div>
                <div className="md-form mt-3">
                  <MDBInput
                    icon="user"
                    label="Your name"
                    iconClass="grey-text"
                    type="text"
                    id="form-name"
                  />
                </div>
                <div className="md-form">
                  <MDBInput
                    icon="envelope"
                    label="Your email"
                    iconClass="grey-text"
                    type="text"
                    id="form-email"
                  />
                </div>
                <div className="md-form">
                  <MDBInput
                    icon="tag"
                    label="Subject"
                    iconClass="grey-text"
                    type="text"
                    id="form-subject"
                  />
                </div>
                <div className="md-form">
                  <MDBInput
                    icon="pencil-alt"
                    label="Your Message"
                    iconClass="grey-text"
                    type="textarea"
                    id="form-text"
                  />
                </div>
                <div className="text-center mt-1">
                  <MDBBtn color="primary" onClick={addProject}>
                    Submit
                  </MDBBtn>
                </div>
              </MDBCardBody>
            </MDBCard>
          </MDBCol>
          <MDBCol lg="7">
            <div
              id="map-container"
              className="rounded z-depth-1-half map-container"
              style={{ height: "400px" }}
            >
              <iframe
                src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d15554.33360246679!2d77.61924415!3d12.934475849999998!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sin!4v1571580290459!5m2!1sen!2sin"
                title="..."
                width="100%"
                height="100%"
                frameBorder="0"
                style={{ border: 0 }}
              />
            </div>
            <br />
            <MDBRow className="justify-content-center text-center text-primary font-weight-bold">
              <MDBCol md="4">
                <MDBBtn
                  href="https://goo.gl/maps/GcpjAbUYxY7jaqFt9"
                  target="blank"
                  tag="a"
                  color="blue"
                  className="accent-1"
                >
                  <MDBIcon icon="map-marker-alt" />
                </MDBBtn>
                <p>
                  Hosur Road, Koramangala
                  <br />
                  Bangalore
                </p>
              </MDBCol>
              <MDBCol md="4">
                <MDBBtn tag="a" floating color="blue" className="accent-1">
                  <MDBIcon icon="phone" />
                </MDBBtn>
                <p>
                  080 1234 5678
                  <br />
                  Mon - Fri
                  <br />
                  8:00 - 22:00
                </p>
              </MDBCol>
              <MDBCol md="4">
                <MDBBtn tag="a" floating color="blue" className="accent-1">
                  <MDBIcon icon="envelope" />
                </MDBBtn>
                <p>
                  info@gmail.com
                  <br />
                  sale@gmail.com
                </p>
              </MDBCol>
            </MDBRow>
          </MDBCol>
        </MDBRow>
      </section>
    </div>
  );
};

export default Contact;
