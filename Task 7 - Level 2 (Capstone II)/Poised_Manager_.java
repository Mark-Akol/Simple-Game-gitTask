import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Date;
import java.util.Scanner;

//This class is used to get the project details from user
public class Poised_Manager_ {

    public static void main(String args[]) {
//Get user input using scanner
        Scanner input = new Scanner(System.in);
//Create an empty list of projects
        ArrayList<Project> projectList = new ArrayList<Project>();
        Project proj = new Project();
//Create objects for architect,customer and contractor
        Person architect = new Person();
        Person customer = new Person();
        Person contractor = new Person();
        System.out.println("Enter a choice:\n1. Add new project\n2. Change due date\n3. Change fee paid to date\n4. Update Contractor's contact details\n5. Finalise the Project ");
//Based on user choice, do the operations
        switch (input.nextInt()) {
            case 1:
//Add a project
                System.out.print("Enter\nProject Number:");
                proj.setProjectNumber(input.nextInt());
                ;
                System.out.println("Project Name");
                proj.setProjectName(input.nextLine());
                System.out.println("typeOfBuilding");
                proj.setTypeOfBuilding(input.nextLine());
                System.out.println("addressOfProject");
                proj.setAddressOfProject(input.nextLine());
                System.out.println("eRFNumber");
                proj.seteRFNumber(input.nextLine());
                System.out.println("totalFee");
                proj.setTotalFee(input.nextDouble());
                System.out.println("totalAmountPaidToDate");
                proj.setTotalAmountPaidDate(input.nextDouble());
                System.out.println("deadline");
                proj.setDeadline(input.nextLine());
                System.out.println("Architect Name");
                architect.setName(input.nextLine());
                System.out.println("Architect phNo");
                architect.setPhoneNo(input.nextLine());
                System.out.println("Architect Email");
                architect.setEmailAddr(input.nextLine());
                System.out.println("Architect address");
                architect.setAddress(input.nextLine());
                proj.setArchitect(architect);
                System.out.println("Contractor Name");
                contractor.setName(input.nextLine());
                System.out.println("Contractor phNo");
                contractor.setPhoneNo(input.nextLine());
                System.out.println("Contractor Email");
                contractor.setEmailAddr(input.nextLine());
                System.out.println("Contractor address");
                contractor.setAddress(input.nextLine());
                proj.setContractor(contractor);
                System.out.println("Customer Name");
                customer.setName(input.nextLine());
                System.out.println("Customer phNo");
                customer.setPhoneNo(input.nextLine());
                System.out.println("Customer Email");
                customer.setEmailAddr(input.nextLine());
                System.out.println("Customer address");
                customer.setAddress(input.nextLine());
                proj.setCustomer(customer);
                projectList.add(proj);
                break;
            case 2:
//Update due date
                System.out.print("Enter project number:");
                int projectNo = input.nextInt();
                input.nextLine();
                System.out.print("Enter new due date:");
                String dueDate = input.nextLine();
                for (Project project : projectList) {
                    if (project.getProjectNumber() == projectNo) {
                        project.setDeadline(dueDate);
                    }
                }
                break;
            case 3:
//Update amount paid
                System.out.print("Enter project number:");
                int projNo = input.nextInt();
                System.out.print("Enter new total amount paid to date:");
                double amountPaid = input.nextDouble();
                for (Project project : projectList) {
                    if (project.getProjectNumber() == projNo) {
                        project.setTotalAmountPaidDate(amountPaid);
                    }
                }
                break;
            case 4:
//Update contractor contact details
                System.out.print("Enter project number:");
                int projectNumber = input.nextInt();
                System.out.print("Enter contractor phone number");
                String phNo = input.nextLine();
                for (Project project : projectList) {
                    if (project.getProjectNumber() == projectNumber) {
                        project.getContractor().setPhoneNo(phNo);
                    }
                }
                break;
            case 5:
//Finalise
                System.out.print("Enter Project number:");
                int proNo = input.nextInt();
                for (Project project : projectList) {
                    if (project.getProjectNumber() == proNo) {
//Generate invoice if there is amount due from customer
                        double amountDue = project.getTotalFee() - project.getTotalAmountPaidDate();
                        if (amountDue > 0)
                            System.out.println(project.generateInvoice(amountDue));
                        FileWriter myWriter;
                        try {
                            myWriter = new FileWriter("CompletedProject.txt");
                            myWriter.write(project.toString());
                            myWriter.write("ProjectStatus:Completed");
                            myWriter.write("Completeion date:" + new Date());
                            myWriter.close();
                        } catch (IOException e) {
                            e.printStackTrace();
                        }

                    }
                }
                break;
        }
    }
}

