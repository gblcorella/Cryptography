/*
 * Gabriel Corella 
 * Applied Cryptography 
 * Sunday February 23, 2020
 *
 *	- Take 10 Paragraphs from the generated Lorem Ipsum Website and deliver the frequency of each letter appeared
 *
 */


public class main {

	public static void main(String[] args) {

		String str = "\n" + 
				"\n" + 
				"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam scelerisque facilisis odio non semper. Vestibulum auctor quam ut quam hendrerit lobortis. Etiam rhoncus bibendum sapien eget iaculis. Curabitur placerat risus lobortis diam dictum, in suscipit tortor lacinia. Curabitur mattis mollis aliquam. Sed quis lacinia tellus. Suspendisse porttitor ante neque, a malesuada ligula ullamcorper sit amet. In pretium sapien libero, in vestibulum tellus semper in. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse eget condimentum odio, eu ultrices justo. Integer quis ipsum vel lacus auctor scelerisque. Duis imperdiet magna ante, et congue quam hendrerit a. Maecenas auctor dolor in vehicula bibendum. Nullam nulla massa, vestibulum sit amet tellus id, dignissim congue neque. Quisque ac urna ac quam imperdiet commodo. Quisque vel ipsum arcu.\n" + 
				"\n" + 
				"Fusce blandit urna porta, eleifend sapien vitae, viverra neque. Proin vitae sem sed lorem lacinia maximus. Curabitur nec quam aliquet, placerat ex vel, vulputate massa. Mauris condimentum, sem vitae porttitor feugiat, odio sapien laoreet ante, at aliquet purus tellus sed nisl. Etiam lectus diam, gravida et nisi eget, vulputate vehicula elit. Morbi in sapien eu nulla accumsan aliquam vitae sit amet libero. Integer lacinia mauris quis lectus posuere, non luctus nulla dictum. Phasellus leo magna, aliquet quis augue vel, convallis sodales quam. Phasellus luctus fermentum sem eu aliquam. Cras non nunc placerat, mollis tellus ac, molestie tortor. Pellentesque molestie justo quis nisi condimentum vehicula. Donec lobortis ante est, id ornare felis ultrices vel.\n" + 
				"\n" + 
				"Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Integer ornare, sem id ornare condimentum, lorem enim efficitur urna, sagittis iaculis est est eget ante. In vel urna sed sapien posuere porta. Mauris eget consectetur nisl. Cras turpis risus, ullamcorper eu lorem quis, tristique feugiat leo. Quisque imperdiet a justo vel tempus. Nunc erat sem, imperdiet in risus ac, condimentum elementum purus. Donec convallis urna felis, nec eleifend nibh porta id. Nullam eu nisl vitae mi accumsan pellentesque. Aliquam ultricies quam at tortor ornare, eu elementum turpis malesuada. Aliquam odio nunc, egestas non faucibus at, sollicitudin id ante. Mauris eleifend elementum velit, at convallis diam viverra id. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\n" + 
				"\n" + 
				"Donec hendrerit tellus id hendrerit aliquam. Quisque tincidunt nisl lectus, at bibendum eros ornare ut. Sed laoreet vel nibh sed gravida. Cras suscipit est at nulla aliquet rhoncus. Donec elit mi, tincidunt ac dolor vitae, vestibulum vulputate mi. Pellentesque vehicula aliquam enim sed facilisis. Duis mollis ipsum ut lorem condimentum, eu ornare mauris faucibus. Aliquam mattis leo eget nunc lobortis, ut elementum leo congue. Cras malesuada mauris augue, sed aliquet ante ornare in.\n" + 
				"\n" + 
				"Phasellus egestas erat magna, ac ultricies nibh vestibulum ornare. Sed quis tellus est. Morbi ultrices, mauris ut pretium tincidunt, nisl nibh scelerisque dui, sit amet pretium metus ante non metus. Duis eleifend sollicitudin purus et pulvinar. Proin pellentesque pulvinar lorem a viverra. Aenean eleifend fringilla odio, eget gravida risus volutpat eu. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse pellentesque efficitur blandit.\n" + 
				"\n" + 
				"Aliquam venenatis turpis sed sem tempor venenatis. Nulla facilisi. Cras dolor justo, porta quis sollicitudin vitae, eleifend interdum orci. Phasellus ac viverra urna, sit amet pharetra elit. In feugiat, est non congue ultricies, risus nisi pharetra diam, vitae sollicitudin nulla velit eu enim. Donec eros eros, euismod vitae arcu vitae, eleifend interdum odio. Donec dignissim volutpat tincidunt. Sed ut quam ut enim gravida fermentum.\n" + 
				"\n" + 
				"Donec porttitor efficitur dapibus. Quisque lorem ante, sodales sit amet lacus ac, aliquam varius nisi. Nam in euismod tortor. Mauris sed egestas justo. In hac habitasse platea dictumst. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nam luctus leo eu sem scelerisque, vitae auctor elit rutrum. Ut hendrerit viverra diam at venenatis. Proin tortor urna, commodo id odio nec, mollis accumsan erat. Fusce nec orci id tortor porttitor sollicitudin. In hac habitasse platea dictumst. Morbi in lorem sit amet libero euismod venenatis ac at tortor. Aliquam bibendum risus vitae lorem finibus finibus. Curabitur quis congue diam. Nunc ac scelerisque mi.\n" + 
				"\n" + 
				"Nulla feugiat turpis vel mollis vehicula. Proin sem lorem, tristique eget augue sed, auctor venenatis metus. Vestibulum pulvinar purus vitae magna feugiat eleifend. Proin quam orci, malesuada sit amet scelerisque sit amet, mattis sit amet diam. Vestibulum nec mollis quam. Cras consequat turpis ultrices ligula varius, at gravida dolor iaculis. Vivamus elit turpis, sagittis eu tincidunt in, consectetur mollis magna.\n" + 
				"\n" + 
				"Fusce neque turpis, pharetra sit amet erat eu, egestas condimentum massa. Maecenas odio tortor, porttitor eget lectus nec, lobortis ultrices odio. Pellentesque maximus mauris sem, vel aliquet augue condimentum convallis. Etiam at felis dapibus, aliquet nibh in, sollicitudin lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aenean magna dui, ornare tincidunt ipsum eu, feugiat porta risus. Quisque ornare lectus metus, sit amet mattis mauris fringilla in. Interdum et malesuada fames ac ante ipsum primis in faucibus. Ut quis magna nec metus luctus vulputate. Etiam justo nisl, tempor eget felis eu, consectetur consectetur tellus. Donec laoreet condimentum varius.\n" + 
				"\n" + 
				"Vivamus scelerisque euismod leo vitae tincidunt. Donec fermentum justo eget ornare vestibulum. Phasellus dictum leo ante. Phasellus faucibus efficitur justo et euismod. Aliquam ullamcorper egestas neque, vitae aliquam diam rhoncus nec. Vivamus nec consectetur nisl. Phasellus vitae odio a ipsum pharetra mollis. Quisque vitae finibus nulla. Suspendisse vitae hendrerit felis, quis dignissim leo. ";
		int[] freq = new int[str.length()];
		int i, j;

		char string[] = str.toCharArray();

		// Convert
		for (i = 0; i < str.length(); i++) {
			freq[i] = 1;
			for (j = i + 1; j < str.length(); j++) {
				if (string[i] == string[j]) {
					freq[i]++;
					string[j] = '0';
				}
			}

		}

		for (i = 0; i < freq.length; i++) {
			if (string[i] != ' ' && string[i] != '0')
				System.out.println("Frequency of " + string[i] + " = " + freq[i]);
		}

	}

}
