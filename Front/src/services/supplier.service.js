import axios from "axios";
const API_URL = 'http://127.0.0.1:4000';

class SupplierService{
    getAllSuppliers(){
        return axios.get(API_URL+'/empresas')
    }
}

export default new SupplierService();
