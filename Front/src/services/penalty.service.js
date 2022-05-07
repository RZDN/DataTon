import axios from "axios";
const API_URL = 'http://127.0.0.1:4000';

class PenaltyService{
    getAllPenaltiesByRuc(ruc){
        return axios.get(API_URL+`/empresas/${ruc}/penalidades`)
    }
}

export default new PenaltyService();
