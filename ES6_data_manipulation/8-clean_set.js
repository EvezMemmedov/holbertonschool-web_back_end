export default function cleanSet (set, stratString) {
  if (!stratString || typeof startString !== 'string') {
    return '';
  }
  return Array.from(set)
    .filter(
      (value) =>
        typeof value === 'string' && value.startsWith(startString)
    )
    .map((value) => value.slice(startString.length))
    .join('-');
}