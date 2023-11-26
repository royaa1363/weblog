import React, { Component } from 'react';
import axios from "axios";

class App extends Component {
    state = {
        blog: []
    };

    componentDidMount() {
    this.getPosts();
    }

    getPosts() {
        axios
            .get('http://127.0.0.1:8000/api/')
            .then(res => {
            this.setState({ blog : res.data });
            })
            .catch(err => {
                console.log(err);
        });
    }
render() {
    return (
        <div>
            {this.state.blog.map(item => (
                <div key={item.id}>
                    <h1>{item.title}</h1>
                    <span>{item.content}</span>
                </div>
            ))}
        </div>
        );
    }
}

export default App;
