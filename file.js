



// Print out all of the strings in the following array in alphabetical order, each on a separate line.
const a = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
// 'Cha Cha'
// 'Foxtrot'
// 'Jive'
// 'Paso Doble'
// 'Rumba'
// 'Samba'
// 'Tango'
// 'Viennese Waltz'
// 'Waltz'

a.sort()
a.forEach(cv => console.log(cv))