import java.lang.reflect.Proxy;


public class MatchMakingTestDrive {

	public static void main(String[] args) {
		MatchMakingTestDrive test = new MatchMakingTestDrive();
		test.drive();
	}
	
	void drive() {
		PersonBean joe = new PersonBeanImpl();
		joe.setName("Joe");
		joe.setGender("M");
		joe.setInterests("computers");
		
		PersonBean ownerProxy = getOwnerProxy(joe);
		ownerProxy.setName("Joe Test");
		ownerProxy.setInterests("computers, soccer");
		try {
			ownerProxy.setHotOrNotRating(5);
		} catch (Exception e) {
			System.out.println("Can't set rating from owner proxy");
		}
		System.out.println("Joe's rating: " + ownerProxy.getHotOrNotRating());
		
		PersonBean nonOwnerProxy = getNonOwnerProxy(joe);
		try {
			nonOwnerProxy.setInterests("food");
		} catch (Exception e) {
			System.out.println("Can't set interests from non owner proxy");
		}
		nonOwnerProxy.setHotOrNotRating(4);
		System.out.println("Joe's rating: " + nonOwnerProxy.getHotOrNotRating());
		
	}
	
	PersonBean getOwnerProxy(PersonBean person) {
		return (PersonBean) Proxy.newProxyInstance(
								person.getClass().getClassLoader(), 
								person.getClass().getInterfaces(), 
								new OwnerInvocationHandler(person));
	}
	
	PersonBean getNonOwnerProxy(PersonBean person) {
		return (PersonBean) Proxy.newProxyInstance(
								person.getClass().getClassLoader(), 
								person.getClass().getInterfaces(), 
								new NonOwnerInvocationHandler(person));
	}
	
}
