import java.lang.reflect.InvocationHandler;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;


public class NonOwnerInvocationHandler implements InvocationHandler {

	PersonBean person;
	
	public NonOwnerInvocationHandler(PersonBean person) {
		this.person = person;
	}
	
	@Override
	public Object invoke(Object proxy, Method method, Object[] args) throws Throwable, IllegalAccessException {
		try {
			if (method.getName().equals("setHotOrNotRating") || method.getName().startsWith("get")) {
				return method.invoke(person, args);
			} else {
				throw new IllegalAccessException();
			}
		} catch (InvocationTargetException e) {
			e.printStackTrace();
		}
		return null;
	}

}
