//This class holds details of customer,architect and contractor
public class Person {
    private String name_;
    private String phone_No;
    private String email_Addr;
    private String address_;

    public String getName() {
        return name_;
    }
    public void setName(String name) {
        this.name_ = name;
    }
    public String getPhoneNo() {
        return phone_No;
    }
    public void setPhoneNo(String phoneNo) {
        this.phone_No = phoneNo;
    }
    public String getEmailAddr() {
        return email_Addr;
    }
    public void setEmailAddr(String emailAddr) {
        this.email_Addr = emailAddr;
    }
    public String getAddress() {
        return address_;
    }
    public void setAddress(String address) {
        this.address_ = address;
    }
}
