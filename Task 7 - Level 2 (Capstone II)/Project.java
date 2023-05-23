//This class holds project details
public class Project {
    private int projectNumber;
    private String projectName;
    private String typeOfBuilding;
    private String addressOfProject;
    private String eRFNumber;
    private double totalFee;
    private double totalAmountPaidToDate;
    private String deadline;
    private Person architect;
    private Person contractor;
    private Person customer;
    //Accessor
    public int getProjectNumber() {
        return projectNumber;
    }
    //Mutator
    public void setProjectNumber(int projectNumber) {
        this.projectNumber = projectNumber;
    }
    public String getProjectName() {
        return projectName;
    }
    public void setProjectName(String projectName) {

        this.projectName=projectName;

    }
    public String getTypeOfBuilding() {
        return typeOfBuilding;
    }
    public void setTypeOfBuilding(String typeOfBuilding) {
        this.typeOfBuilding = typeOfBuilding;
    }
    public String getAddressOfProject() {
        return addressOfProject;
    }
    public void setAddressOfProject(String addressOfProject) {
        this.addressOfProject = addressOfProject;
    }
    public String geteRFNumber() {
        return eRFNumber;
    }
    public void seteRFNumber(String eRFNumber) {
        this.eRFNumber = eRFNumber;
    }
    public double getTotalFee() {
        return totalFee;
    }
    public void setTotalFee(double totalFee) {
        this.totalFee = totalFee;
    }
    public double getTotalAmountPaidDate() {
        return totalAmountPaidToDate;
    }
    public void setTotalAmountPaidDate(double totalAmountPaidDate) {
        this.totalAmountPaidToDate = totalAmountPaidDate;
    }
    public String getDeadline() {
        return deadline;
    }
    public void setDeadline(String deadline) {
        this.deadline = deadline;
    }


    public Person getArchitect() {
        return architect;
    }
    public void setArchitect(Person architect) {
        this.architect = architect;
    }
    public Person getContractor() {
        return contractor;
    }
    public void setContractor(Person contractor) {
        this.contractor = contractor;
    }
    public Person getCustomer() {
        return customer;
    }
    public void setCustomer(Person customer) {
        this.customer = customer;
    }
//This method generates invoice as per the format

    public String generateInvoice(double amount)
    {
        return customer.toString()+"Amount due:"+amount + " to be paid by customer";

    }
    @Override
    public String toString() {
        return "Project [projectNumber=" + projectNumber + ", projectName=" + projectName + ", typeOfBuilding="
                + typeOfBuilding + ", addressOfProject=" + addressOfProject + ", eRFNumber=" + eRFNumber + ", totalFee="
                + totalFee + ", totalAmountPaidToDate=" + totalAmountPaidToDate + ", deadline=" + deadline + ", architect="
                + architect + ", contractor=" + contractor + ", customer=" + customer + "]";
    }


}