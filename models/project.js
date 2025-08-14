class Project {
  constructor({id, client, startDate, endDate, status}) {
    this.id = id;
    this.client = client;
    this.startDate = startDate;
    this.endDate = endDate;
    this.status = status;
    this.menu = null;
    this.resources = {
      equipment: [],
      personnel: [],
      products: []
    };
  }
}

module.exports = Project;
