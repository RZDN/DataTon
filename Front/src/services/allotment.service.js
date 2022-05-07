import axios from "axios";
const API_URL = 'http://127.0.0.1:4000';

class AllotmentService{
    getAllAllotmentsByRuc(ruc){
        return axios.get(API_URL+`/empresas/${ruc}/adjudicaciones`)
    }
}

export default new AllotmentService();
