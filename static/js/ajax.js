class httpClient {
    constructor(){
        this.httpRequest = new XMLHttpRequest();
        this.requests    = {};
        this.request_id  = '';
        if (!this.httpRequest) {
            throw('Cannot create an XMLHTTP instance');
        }
        this.httpRequest.onreadystatechange = this.ReadyStateChange;
    }

    get(url) {
        return this.makeRequest("GET", url);
    }

    post(url){
        return this.makeRequest("POST", url);
    }

    makeRequest(method, url) {
        this.request_id = uuid();
        this.requests[this.request_id] = {"state": "pending", "method": method, "url": url};
        this.httpRequest.open(method, url);
        this.httpRequest.send();
        return this.request_id;
    }

    ReadyStateChange() {
        if (this.httpRequest.readyState === XMLHttpRequest.DONE) {
            this.requests[this.request_id]['state'] = "complete";
            this.requests[this.request_id]['status'] = this.httpRequest.status;
            if (this.httpRequest.status === 200) {
                this.requests[this.request_id]['httpRequest'] = this.httpRequest;
            }
        }
    }
}